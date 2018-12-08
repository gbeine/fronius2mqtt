from setuptools import setup

setup(name='fronius2mqtt',
      version='0.1',
      description='Fronius 2 MQTT bridge',
      url='https://github.com/gbeine/fronius2mqtt',
      author='Gerrit',
      author_email='mail@gerritbeine.de',
      license='MIT',
      packages=['fronius2mqtt'],
      requires=[
          'logging',
          'paho.mqtt',
          'pyfronius',
          'pyyaml',
        ],
      zip_safe=False)
