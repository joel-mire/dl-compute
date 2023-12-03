import aws_cdk as core
import aws_cdk.assertions as assertions

from basic_dl_compute.basic_dl_compute_stack import BasicDlComputeStack

# example tests. To run these tests, uncomment this file along with the example
# resource in basic_dl_compute/basic_dl_compute_stack.py
def test_sqs_queue_created():
    app = core.App()
    stack = BasicDlComputeStack(app, "basic-dl-compute")
    template = assertions.Template.from_stack(stack)

#     template.has_resource_properties("AWS::SQS::Queue", {
#         "VisibilityTimeout": 300
#     })
