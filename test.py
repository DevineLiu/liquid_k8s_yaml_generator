import liquid_k8s_yaml_generator



yaml_fb = liquid_k8s_yaml_generator.template.render(
image_name="test-demo", #被应用于作为服务、istio vs、应用名、sls 的名字的生成 禁止下划线
replicas=2, 
remote_image_name="ubuntu:latest" , # 镜像地址
port = 80, #应用开放的端口
env_items = {"KEY":"vaule"}, #环境变量
log_path = "/log/*log" , #sls 采集日志的地址
address_type ="sd"
)

print(yaml_fb)
