from distutils.core import setup
setup(
  name = 'weballurl',         # How you named your package folder (MyLib)
  packages = ['weballurl'],   # Chose the same as "name"
  version = '1.1.6',      # Start with a small number and increase it with every change you make
  license='MIT',        # Chose a license from here: https://help.github.com/articles/licensing-a-repository
  description = '获取一个指定网站所有的本站url；Gets all site urls for a specified site',   # Give a short description about your library
  author = 'zyg0531',                   # Type in your name
  author_email = '1455857826@qq.com',      # Type in your E-Mail
  url = 'https://github.com/zhangyg531/weballurl',   # Provide either the link to your github or to your website
  download_url = 'https://codeload.github.com/zhangyg531/weballurl/zip/refs/heads/main',    # I explain this later on
  keywords = ['url', 'allurl', 'wenallurl'],   # Keywords that define your package best
  install_requires=[            # I get to this in a second
          'requests',       # 可以加上版本号，如validators=1.5.1
          'fake_useragent',
      ],
  classifiers=[
    'Development Status :: 3 - Alpha',      # Chose either "3 - Alpha", "4 - Beta" or "5 - Production/Stable" as the current state of your package
    'Intended Audience :: Developers',      # Define that your audience are developers
    'Topic :: Software Development :: Build Tools',
    'License :: OSI Approved :: MIT License',   # Again, pick a license
    'Programming Language :: Python :: 3',
    'Programming Language :: Python :: 3.6',
    'Programming Language :: Python :: 3.8',
  ],
)