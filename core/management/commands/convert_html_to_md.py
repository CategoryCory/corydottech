import html2text
from django.core.management.base import BaseCommand, CommandError, CommandParser
from django.apps import apps


class Command(BaseCommand):
    help = (
        "Convert HTML to Markdown for a given model\'s text field. "
        "Usage: manage.py convert_html_to_md <app_name>.<model_name> [--field <field_name>]"
    )

    def add_arguments(self, parser: CommandParser) -> None:
        parser.add_argument(
            "model",
            type=str,
            help="The model to convert HTML to Markdown for.",
        )
        parser.add_argument(
            "--field",
            type=str,
            default="description",
            help="The field to convert HTML to Markdown for (default 'description').",
        )
        parser.add_argument(
            "--batch-size",
            type=int,
            default=100,
            help="The number of records to convert at a time (default 100).",
        )

    def handle(self, *args, **options) -> None:
        label = options["model"]
        field = options["field"]
        batch_size = options["batch_size"]

        try:
            app_label, model_name = label.split(".")
        except ValueError:
            raise CommandError(f"Please use format <app_name>.<model_name>.")

        mdl = apps.get_model(app_label, model_name)
        if mdl is None:
            raise CommandError(f"Model '{label}' not found.")

        qs = mdl.objects.all()
        total = qs.count()
        self.stdout.write(f"Converting {total} {label} records...")

        md_converter = html2text.HTML2Text()
        md_converter.ignore_links = False

        for start in range(0, total, batch_size):
            for obj in qs[start : start + batch_size]:
                html = getattr(obj, field, "") or ""
                new_md = md_converter.handle(html)
                setattr(obj, field, new_md)
                obj.save(update_fields=[field])
                self.stdout.write(f"\t- {label} {obj.pk} converted.")

        self.stdout.write(f"Finished converting {total} {label} records.")
