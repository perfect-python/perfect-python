from distutils.core import setup, Extension

setup(name='dumb_print',
        version='1.0',
        ext_modules=[Extension('dumb_print', ['dumb_print.c'])],
)

# setup(name='spam_type1',
#         version='1.0',
#         ext_modules=[Extension('spam', ['spam_type1.c'])],
# )

# setup(name='spam_type2',
#         version='1.0',
#         ext_modules=[Extension('spam', ['spam_type2.c'])],
# )
