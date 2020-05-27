#from python_terraform import *

#tf = Terraform(working_dir='/var/lib/jenkins/workspace/Terraform-Python/infra')
#tf.plan(out="plan.out", lock = False)
#approve = {"auto-approve": True}
#print(tf.init(reconfigure=True))
#print(tf.apply(skip_plan = True, lock= False))
#print(tf.apply("plan.out", skip_plan= True))

from python_terraform import *

tf = Terraform(working_dir='/var/lib/jenkins/workspace/Terraform-Python/infra')
tf.plan()
print(tf.init(reconfigure=True))
print(tf.apply(skip_plan = True))
