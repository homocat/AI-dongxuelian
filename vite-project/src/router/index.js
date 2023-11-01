import { createRouter, createWebHashHistory } from "vue-router";

import Home from "../view/Home.vue"

const routes = [
  {
    path: "/",
    component: () => import("../view/Home.vue"),
    children: [
      {
        path: "/todolist",
        component: () => import("../view/Home/TodoList.vue")
      },
      {
        path: "/health",
        component: () => import("../view/Health.vue")
      },
      {
        path: "/about",
        component: () => import("../view/About.vue")
      },
      {
        path: "/spark",
        component: () => import("../view/Spark.vue")
      }
    ]
  },
  {
    path: "/login",
    component: () => import("../view/Login.vue")
  },

  {
    path: "/:pathMatch(.*)*",
    name: "NotFound",
    component: () => import("../view/404.vue")
  },
]

const router = createRouter({
  history: createWebHashHistory(),
  routes,
});

export default router;