import arrow
from jinja2.ext import Extension


class ArrowExtension(Extension):
    def __init__(self, environment):
        super(ArrowExtension, self).__init__(environment)

        def year(datetime_obj):
            return arrow.get(datetime_obj).year

        def humanize(datetime_obj):
            a = arrow.get(datetime_obj)
            return a.humanize()

        def date_format(datetime_obj):
            a = arrow.get(datetime_obj)
            return a.format("MMMM D, YYYY")

        def time_format(datetime_obj):
            a = arrow.get(datetime_obj)
            return a.format("h:mm a").replace(":00", "")

        arrow_filters = dict(
            year=year,
            humanize_arrow=humanize,
            format_date=date_format,
            format_time=time_format,
        )
        environment.filters.update(arrow_filters)
