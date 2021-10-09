import Vue from 'vue'
import Element from 'element-ui'
import '../element-variables.scss'
import {Message} from 'element-ui'

Vue.use(Element)
Vue.prototype.$message = Message;