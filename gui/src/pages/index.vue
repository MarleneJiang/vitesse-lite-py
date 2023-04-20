<script setup lang="ts" generic="T extends any, O extends any">
defineOptions({
  name: 'IndexPage',
})


let creator = $ref('')

onMounted(() => {
  py2Js() // 挂载函数，供给python调用
})

const getOwner = () => {
  window.pywebview.api.getOwner().then((res) => {
    creator = res
  })
}

const py2Js = () => {
  // 挂载函数，供给python调用
  window['py2js'] = (resJson) => {
    const res = JSON.parse(resJson)
    console.log(res)
  }
}

</script>

<template>
  <div>
    <div i-carbon-campsite inline-block text-4xl />
    <p>
      <a rel="noreferrer" href="https://github.com/antfu/vitesse-lite" target="_blank">
        vitesse-lite-py
      </a>
    </p>
    <p>
      <em text-sm op75>vitesse+pywebview</em>
    </p>

    <div py-4 />

    <TheInput
      v-model="creator"
      placeholder="用戶名稱？"
      autocomplete="false"
      @keydown.enter="getOwner"
    />

    <div>
      <button
        class="m-3 text-sm btn"
        :disabled="!!creator"
        @click="getOwner"
      >
        獲取
      </button>
    </div>
  </div>
</template>
