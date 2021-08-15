import { createApp } from 'vue'
import App from './App.vue'
import router from './router'
import {store} from './store'
import {library} from "@fortawesome/fontawesome-svg-core";
import {FontAwesomeIcon} from "@fortawesome/vue-fontawesome";
import {fas} from '@fortawesome/free-solid-svg-icons'

library.add(fas);
import {fab} from '@fortawesome/free-brands-svg-icons';

library.add(fab);
import {far} from '@fortawesome/free-regular-svg-icons';

library.add(far);
import {dom} from "@fortawesome/fontawesome-svg-core";

dom.watch();
import {QuillEditor} from '@vueup/vue-quill'
import '@vueup/vue-quill/dist/vue-quill.snow.css';


createApp(App)
    .use(store)
    .use(router)
    .component('QuillEditor', QuillEditor)
    .component('font-awesome-icon', FontAwesomeIcon)
    .mount('#app')
