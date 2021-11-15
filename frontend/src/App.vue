<template>
  <v-app>
    <v-container fluid>
      <v-row align="start" justify="center">
        <v-col cols="10">
          <v-textarea
          outlined
          name="input-7-4"
          label="テキストを入力してください"
          v-model="InputText"
        ></v-textarea>
        <v-textarea
          outlined
          name="input-7-4"
          label="テキストを入力してください"
          v-model="InputText2"
        ></v-textarea>
        </v-col>
        <v-col cols="2">
          <v-btn outlined @click="SendData"> 文字数をカウント </v-btn>
        </v-col>
      </v-row>

      <v-row align="start" justify="center">
        <v-col cols="6">
        <v-card
          max-width="450"
          class="mx-auto"
        >
          <v-toolbar
            dark
          >
            <v-toolbar-title>Result</v-toolbar-title>
          </v-toolbar>

          <v-list three-line>
            <template v-for="(item, index) in items">
              <v-list-item
                :key="item.title"
              >
                <v-list-item-content>
                  <v-list-item-title >{{ item.count }}文字です</v-list-item-title>
                  <v-list-item-subtitle> {{ item.text }} </v-list-item-subtitle>
                </v-list-item-content>
              </v-list-item>
              <v-divider
                :key="index"
                :inset="item.inset"
              ></v-divider>
            </template>
          </v-list>
        </v-card>
        </v-col>
      </v-row>
    </v-container>
  </v-app>
</template>

<script>
import axios from 'axios'

export default {
  name: 'App',

  data () {
    return {
      // 入力データ
      InputText: '',
      TextLength: null,
      items: []
    }
  },

  methods: {
    SendData: function () {
      var data = { text: this.InputText }

      axios
        .post('/api/post', data)
        .then(response => {
          this.items.push(response.data)
        })
        // .catch(err => {
        //   alert('APIサーバと接続できません')
        //   err = null
        // })
    }
  }
}
</script>