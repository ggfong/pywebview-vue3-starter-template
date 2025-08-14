import antfu from '@antfu/eslint-config'

export default antfu({
  languageOptions: {
    globals: {
      ElMessage: 'readonly',
    },
  },
})
