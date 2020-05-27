from python_terraform import *

tf = Terraform(working_dir='/var/lib/jenkins/workspace/Terraform-Python/infra')
tf.plan(no_color=IsFlagged, refresh=False, capture_output=True, out="plan.out")
#tf.plan(out="plan.out", lock = False)
#approve = {"auto-approve": True}
print(tf.init(reconfigure=True))
#print(tf.apply(skip_plan = True, lock= False))
print(tf.apply("plan.out", skip_plan= True))

