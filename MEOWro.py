from click import command, option, Option, UsageError


class MEOWro(Option):
    
    def __init__(self, *args, **kwargs):
        self.mutually_exclusive = set(kwargs.pop('mutually_exclusive', []))
        self.required_options = set(kwargs.pop('required_options', []))
        help = kwargs.get('help', '')
        if self.mutually_exclusive:
            ex_str = ', '.join(self.mutually_exclusive)
            kwargs['help'] = help + (
                ' NOTE: This argument is mutually exclusive with '
                ' arguments: [' + ex_str + '].'
            )
        if self.required_options:
            ex_str = ', '.join(self.required_options)
            kwargs['help'] = help + (
                ' NOTE: This argument requires  '
                ' options: [' + ex_str + '] to be provided.'
            )

        super(MEOWro, self).__init__(*args, **kwargs)

    def handle_parse_result(self, ctx, opts, args):
        if self.mutually_exclusive.intersection(opts) and self.name in opts:
            raise UsageError(
                "Illegal usage: `{}` is mutually exclusive with "
                "arguments `{}`.".format(
                    self.name,
                    ', '.join(self.mutually_exclusive)
                )
            )

        if not self.required_options.intersection(opts) and self.name in opts:
            raise UsageError(
                "Illegal usage: `{}` requires "
                "options `{}` to be provided.".format(
                    self.name,
                    ', '.join(self.required_options)
                ) 
            )

        return super(MEOWro, self).handle_parse_result(
            ctx,
            opts,
            args
        )