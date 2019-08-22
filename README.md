# liquid_k8s_yaml_generator
用于生成简单的k8s yaml配置文件

##install 
```bash 
pip install git+https://github.com/DevineLiu/liquid_k8s_yaml_generator.git@master
```

##usage

```python
import liquid_k8s_yaml_generator

yaml_fb = liquid_k8s_yaml_generator.template.render(
image_name="test-demo", #被应用于作为服务、istio vs、应用名、sls 的名字的生成 禁止下划线
replicas=2,
remote_image_name="ubuntu:latest" , # 镜像地址
port = 80, #应用开放的端口
env_items = {"KEY":"vaule"}, #环境变量
log_path = "/log/*log"  #sls 采集日志的地址
)

print(yaml_fb)
```

###stdout:
```
apiVersion: apps/v1beta2
kind: Deployment
metadata:
  name: test-demo
  namespace: default
spec:
  replicas: 2
  selector:
    matchLabels:
      app: test-demo
  template:
    metadata:
      labels:
        app: test-demo
    spec:
      containers:
        - name: test-demo
          image: 'ubuntu:latest'
          env:
            ######### 配置 环境变量 ###########
            - name: KEY
              value: vaule
            - name: aliyun_logs_test-demo-stdout
              value: stdout
            - name: aliyun_logs_test-demo-log
              value: /log/*log
          ports:
            - containerPort: 80
  ###############################

---
apiVersion: v1
kind: Service
metadata:
  name: test-demo-svc
  labels:
    app: test-demo
    service: test-demo
spec:
  ports:
    - port: 80
      name: test-demo-svc
  selector:
    app: test-demo
  type: LoadBalancer

---
apiVersion: networking.istio.io/v1alpha3
kind: VirtualService
metadata:
  name: test-demo-vs
  namespace: default
spec:
  hosts:
    - test-demo-vs-svc
  http:
    - route:
        - destination:
            host: test-demo-svc
            subset: test-demo-svc

---
apiVersion: v1
kind: Service
metadata:
  name: test-demo-vs-svc
  labels:
    app: test-demo-vs
    service: test-demo-vs
spec:
  ports:
    - port: 80
      name: test-demo-vs-svc
      targetPort: 80
  selector:
    app: test-demo
  type: LoadBalancer
 ```
