class link_builder(object):

    link_template = "<a href='{url}' {target}>{name}</a>"

    def __init__(self, url, name, target=None):
        self.url = url
        self.name = name
        self.target = "target = '%s'" % target if target else ""

    def __repr__(self):
        return self.link_template.format(name=self.name, target=self.target, url=self.url)

class link_builder2(object):
    link_template = "<a href='{url}' {target}>{name}</a>"

    @classmethod
    def make_link(cls, url, name, target=None):
        return cls.link_template.format(name=name, target="target = '%s'" % target if target else '', url=url)

class link_builder3(object):
    link_template = "<a href='%(url)s' %(target)s %(attrs)s>%(name)s</a>"

    @classmethod
    def make_link(cls, **kwargs):
        # return cls.link_template.format(**kwargs)
        attrs = []
        # print type(kwargs.get('attrs'))
        for k, v in kwargs.get('attrs').items():
            attrs.append(" %s='%s'" % (k, v))

        return cls.link_template % {
                'name': kwargs.get('name'),
                'target': "target='%s'" % kwargs.get('target') if kwargs.get('target') else '',
                'url': kwargs.get('url'),
                'attrs': ''.join(attrs),
        }