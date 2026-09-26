from setuptools import find_packages, setup

package_name = 'navigrid_safety'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
    data_files=[
        ('share/ament_index/resource_index/packages',
            ['resource/' + package_name]),
        ('share/' + package_name, ['package.xml']),
    ],
    install_requires=['setuptools'],
    zip_safe=True,
    maintainer='navab',
    maintainer_email='24f2001508@ds.study.iitm.ac.in',
    description='TODO: Package description',
    license='TODO: License declaration',
    extras_require={
        'test': [
            'pytest',
        ],
    },
    entry_points={
	'console_scripts': [
    		'safety_override = navigrid_safety.safety_override:main',
    		'test_scan = navigrid_safety.test_scan:main',
	],
    },
)
