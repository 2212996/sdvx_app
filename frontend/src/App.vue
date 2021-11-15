<template>
  <v-app>
    <v-container fluid>
      <v-row align="start" justify="center">
        <v-col cols="10">
          <v-textarea
          outlined
          name="input-7-4"
          label="自分のユーザーID"
          v-model="InputUser1"
        ></v-textarea>
        <v-textarea
          outlined
          name="input-7-4"
          label="ライバルのユーザーID"
          v-model="InputUser2"
        ></v-textarea>
        <v-textarea
          outlined
          name="input-7-4"
          label="選択する難易度"
          v-model="InputDifficulty"
          type="number"
        ></v-textarea>
        <v-textarea
          outlined
          name="input-7-4"
          label="スコア差"
          v-model="InputScoreGap"
          type="number"
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
                  <v-list-item-title >{{ item.title }}</v-list-item-title>
                  <v-list-item-subtitle> {{ item.gap }} </v-list-item-subtitle>
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
      InputUser1: '221sdvx',
      InputUser2: 'ddr_das',
      InputDifficulty: '19',
      InputScoreGap: '30000',
      items: []
    }
  },

  methods: {
    SendData: function () {
      var data = { user1: this.InputUser1,
       user2: this.InputUser2,
       difficulty: this.InputDifficulty,
       gap: this.InputScoreGap}

      axios
        .post('/post', data)
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