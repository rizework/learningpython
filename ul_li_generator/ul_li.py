class ul_li(object):
    template = '<li%(class)s>%(value)s</li>'

    def _html_output(self, list, css_class):
        output = []
        css_class = '' if None else " class='%s'" % css_class
        for item in list:
            output.append(self.template % {'value': item, 'class': css_class})
        return '\n'.join(output)

    def generate(self, list, css_class=None):
        return self._html_output(list, css_class)


