import arrow
from jinja2.ext import Extension
from datetime import datetime
from jinja2.environment import Environment


class ArrowExtension(Extension):
    def __init__(self, environment: Environment) -> None:
        super().__init__(environment)

        def year(datetime_obj: datetime) -> str:
            return str(arrow.get(datetime_obj).year)

        def humanize(datetime_obj: datetime) -> str:
            return arrow.get(datetime_obj).humanize()

        def date_format(datetime_obj: datetime) -> str:
            return arrow.get(datetime_obj).format("MMMM D, YYYY")

        def time_format(datetime_obj: datetime) -> str:
            return arrow.get(datetime_obj).format("h:mm a").replace(":00", "")

        arrow_filters = dict(
            year=year,
            humanize_arrow=humanize,
            format_date=date_format,
            format_time=time_format,
        )
        environment.filters.update(arrow_filters)  # type: ignore
