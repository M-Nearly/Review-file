| 名称                      | 缩写 | 作用                                                         | 举例                                                         |
| ------------------------- | ---- | ------------------------------------------------------------ | ------------------------------------------------------------ |
| `v-if, v-else-if, v-else` | none | 条件渲染                                                     | `<g v-if="flourish === 'A'"></g><g v-else-if="flourish === 'B'"></g><g v-else></g>` |
| `v-bind`                  | :    | 动态地绑定一个或多个特性，或一个组件 prop 到表达式           | `<div :style="{ background: color }"></div>`                 |
| `v-on`                    | @    | 绑定事件监听器到元素                                         | `<button @click="fnName"></button>`                          |
| `v-model`                 | none | 创建双向绑定                                                 | `<textarea rows="5" v-model="message" maxlength="72"></textarea>` |
| `v-pre`                   | none | 跳过原始内容的编译过程，可以提高性能                         | `<div v-pre>{{ raw content with no methods}}</div>`          |
| `v-once`                  | none | 不渲染                                                       | `<div class=”v-once”>Keep me from rerendering</div>`         |
| `v-show`                  | none | 根据状态显示或者隐藏组件/元素，但是会保存在 DOM 中不会销毁 (不同于 v-if) | `<child v-show=”showComponent”></child>`(当 showComponent 为 true 时切换可见性) |

