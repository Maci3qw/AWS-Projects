import boto3

region = 'eu-west-1'
ec2 = boto3.client('ec2', region_name=region)


def lambda_handler(event, context):
    instances = event["instances_id"]
    action = event["action"]
    status = ec2.describe_instance_status(InstanceIds=instances, IncludeAllInstances=True)   
    instance_status = status['InstanceStatuses'][0]['InstanceState']['Code']
   
    
    
    
    
    if action=="Start": 
        ec2.start_instances(InstanceIds=instances)
        print(status)
        print("Instance has been started!")
    elif action=="Stop": 
        ec2.stop_instances(InstanceIds=instances)
        print("Instance status =", instance_status)
        print("Instance has been stopped!")
    elif action=="":
        print("is null")
    else:
        print("Type correct command")
