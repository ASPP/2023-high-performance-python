project('integrate_f6', 'cython',
        version : '0',
        license : 'BSD0')

# For documentation, see:
# https://mesonbuild.com/Python-module.html
# https://mesonbuild.com/Cython.html

py = import('python').find_installation()

py.extension_module(
  'integrate_f6',
  'integrate_f6.pyx',
  dependencies : py.dependency(),
  install : true,
)
