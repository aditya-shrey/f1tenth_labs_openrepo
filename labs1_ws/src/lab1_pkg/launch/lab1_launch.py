def generate_launch_description():
    return LaunchDescription([
        Node(
            package='lab1_pkg',
            executable='python3',
            arguments=['/lab1_ws/src/lab1_pkg/src/talker.py'],
            name='talker',
            parameters=[
                {'v': 0.5},
                {'d': 0.0}
            ]
        ),
        Node(
            package='lab1_pkg',
            executable='python3',
            arguments=['/lab1_ws/src/lab1_pkg/src/relay.py'],
            name='relay'
        )
    ])
