from setuptools import find_packages, setup

package_name = 'navigrid_navigation'

setup(
    name=package_name,
    version='0.0.0',
    packages=find_packages(exclude=['test']),
data_files=[
    ('share/ament_index/resource_index/packages',
        ['resource/navigrid_navigation']),
    ('share/navigrid_navigation',
        ['package.xml']),
('share/navigrid_navigation/config',
    [
        'config/nav2_params.yaml',
        'config/slam_toolbox.yaml',
    ]),
('share/navigrid_navigation/launch',
 ['launch/navigation.launch.py']),
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
        'odom_tf_broadcaster = navigrid_navigation.odom_tf_broadcaster:main',
    ],
},
)
