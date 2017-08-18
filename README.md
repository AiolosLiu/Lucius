# Kobe

The system is using Amazon Web Services and ROS to realize using voice to control Turtlebot's movement.

The project are divided into two parts. One is in the cloud - AWS. we use Alexa assistant to translate the voice to texts. Then using AWS Lambda function send control commands to the local server by Http request. 

In the local part, when the server receives the the commands, it can execute the relation script. The turtle box moves finally.
