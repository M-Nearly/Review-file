


``` python
from django.form import modelPto_dict()

# breadcrumb_list.insert(0, {"id": parent.id, "name": parent.name})
# 上面等同于 导入模块, 把需要的字段写到列表内
breadcrumb_list.insert(0, model_to_dict(parent, ["id", "name"]))
```



可以直接通过 form 将 model 中转换为字典



