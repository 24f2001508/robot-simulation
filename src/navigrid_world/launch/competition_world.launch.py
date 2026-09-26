from launch import LaunchDescription
from launch.actions import ExecuteProcess
from ament_index_python.packages import get_package_share_directory
import os


def generate_launch_description():

    world_file = os.path.join(
        get_package_share_directory('navigrid_world'),
        'worlds',
        'competition_world.sdf'
    )

    return LaunchDescription([
        ExecuteProcess(
            cmd=['gz', 'sim', world_file],
            output='screen'
        )
    ])
