from link_builder_class import link_builder, link_builder2, link_builder3

l = link_builder(name='google', url='http://www.google.com', target='_blank')
print l
#  <a href='http://www.google.com' target=''>google</a> output

print link_builder2.make_link(name='google', url='http://www.google.com')


class my_link_build(link_builder2):
    @classmethod
    def make_link(cls, url, name, target=None):
        return "hello from my link build"


print my_link_build.make_link(name='google', url='http://www.google.com')

print link_builder3.make_link(name='google', url='http://www.google.com', target='_blank',
                              attrs={'class': 'link-item', 'color': 'blue'}
                              )

