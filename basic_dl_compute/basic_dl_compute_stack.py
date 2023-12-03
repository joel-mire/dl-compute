from aws_cdk import (
    Stack
)
from constructs import Construct
import aws_cdk.aws_ec2 as ec2


class BasicDlComputeStack(Stack):

    def __init__(self, scope: Construct, construct_id: str, **kwargs) -> None:
        super().__init__(scope, construct_id, **kwargs)

        # default VPC
        vpc = ec2.Vpc.from_lookup(self, "VPC", is_default=True)

        instance = ec2.Instance(
            self,
            "Instance",
            # If updating either the instance type or AMI, check the AMI documentation to verify that the AMI is
            # compatible with the instance type
            instance_type=ec2.InstanceType('g4dn.xlarge'),
            machine_image=ec2.MachineImage.lookup(name='Deep Learning AMI GPU PyTorch 2.1.0 (Ubuntu 20.04) 20231103'),
            vpc=vpc,
            instance_name='dl',
            # Assumes that this key-pair has been created in advance. If creating the key-pair for the first time,
            # be sure to save the private key pem file locally to enable SSH to the instance
            key_name='key-pair'
        )

        volume = ec2.CfnVolume(
            self,
            "Volume",
            availability_zone=instance.instance_availability_zone,
            volume_type='gp3',
            size=32
        )

        volume_attachment = ec2.CfnVolumeAttachment(
            self,
            "VolumeAttachment",
            instance_id=instance.instance_id,
            volume_id=volume.attr_volume_id,
            device='/dev/sdf'
        )