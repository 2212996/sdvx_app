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
          <v-slider
            thumb-label
            max="20"
            min="1"
          ></v-slider>
        </v-col>
        <v-col
          cols="12"
          sm="4"
          md="4"
        >
          <v-checkbox
            v-model="selected"
            label="John"
            value="NOV"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="Jacob"
            value="ADV"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="John"
            value="EXH"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="Jacob"
            value="INF"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="Jacob"
            value="GRV"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="John"
            value="HVN"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="Jacob"
            value="VVD"
          ></v-checkbox>
          <v-checkbox
            v-model="selected"
            label="Jacob"
            value="MXM"
          ></v-checkbox>
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

    <v-container>

      <v-row>
        <v-col>
          <v-textarea
          outlined
          label="your_id"
          name="your_id"
          v-model="your_id"
          ></v-textarea>
        </v-col>
        <v-col>
          <v-textarea
          outlined
          label="opp_id"
          name="opp_id"
          v-model="opp_id"
          ></v-textarea>
        </v-col>
      </v-row>
      <span>あなたのID: {{ your_id }}</span>
      <span>相手のID: {{ opp_id }}</span>

      <v-row>
        <v-col>
          <v-slider
            thumb-label
            v-model="selected_minlevel"
            label="minlevel"
            value="minlevel"
            max="20"
            min="1"
          ></v-slider>
        </v-col>
        <v-col>
          <v-slider
            thumb-label
            v-model="selected_maxlevel"
            label="maxlevel"
            value="maxlevel"
            max="20"
            min="1"
          ></v-slider>
        </v-col>
      </v-row>
      <span>選択した最低レベル: {{ selected_minlevel }}</span>
      <span>選択した最高レベル: {{ selected_maxlevel }}</span>

      <v-row>
        <v-col
          v-for="tmp in difficulty"
          :key="tmp.k"
        >
          <v-checkbox
            v-model="selected_diff"
            :label="tmp.label"
            :value="tmp.value"
          ></v-checkbox>
        </v-col>
      </v-row>
      <span>選択した難易度: {{ selected_diff }}</span>

      <v-row>
        <v-col
          v-for="tmp in clearmark"
          :key="tmp.k"
        >
          <v-checkbox
            v-model="selected_clearlamp"
            :label="tmp.label"
            :value="tmp.value"
          ></v-checkbox>
        </v-col>
      </v-row>
      <span>選択したクリアランプ: {{ selected_clearlamp }}</span>

      <v-row>
        <v-col
          v-for="tmp in grade"
          :key="tmp.k"
        >
          <v-checkbox
            v-model="selected_grade"
            :label="tmp.label"
            :value="tmp.value"
          ></v-checkbox>
        </v-col>
      </v-row>
      <span>選択したグレード: {{ selected_grade }}</span>

      <v-row>
        <v-col
          v-for="tmp in scoregap"
          :key="tmp.k"
        >
          <v-slider
            thumb-label
            step="5000"
            v-model="selected_scoregap"
            :label="tmp.label"
            :max="MaxScoreGap"
            :min="MinScoreGap"
          ></v-slider>
        </v-col>
      </v-row>
      <span>選択したスコア差: {{ selected_scoregap }}</span>

      <v-row>
        <v-col>
          <v-btn outlined @click="SendDatas"> 実行！！ </v-btn>
        </v-col>
      </v-row>

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
      items: [],
      max: 20,
      min: 1,
      MaxScoreGap:100000,
      MinScoreGap:0,
      your_id: '',
      opp_id: '',
      selected_minlevel: [],
      selected_maxlevel: [],
      selected_diff: [],
      selected_clearlamp: [],
      selected_grade: [],
      selected_scoregap: [],
    }
  },

  computed: {
    difficulty() {
      return [
        { key: "0", label: "NOV", value: "novice" },
        { key: "1", label: "ADV", value: "advance" },
        { key: "2", label: "EXH", value: "exhaust" },
        { key: "3", label: "INF", value: "infinite" },
        { key: "4", label: "GRV", value: "gravity" },
        { key: "5", label: "HVN", value: "heavenly" },
        { key: "6", label: "VVD", value: "vivid" },
        { key: "7", label: "MXM", value: "maximum" }
      ];
    },
    clearmark(){
       return [
          { key: "0", label: "NO PLAY", value: "NO PLAY" },
          { key: "1", label: "CRASH", value: "CRASH" },
          { key: "2", label: "COMP", value: "COMP" },
          { key: "3", label: "EX COMP", value: "EXCOMP" },
          { key: "4", label: "UC", value: "UC" },
          { key: "5", label: "PUC", value: "PER" }
       ]
    },
    grade(){
       return [
          { key: "0", label: "F", value: "F" },
          { key: "1", label: "D", value: "D" },
          { key: "2", label: "C", value: "C" },
          { key: "3", label: "B", value: "B" },
          { key: "4", label: "A", value: "A" },
          { key: "5", label: "A+", value: "A+" },
          { key: "6", label: "AA", value: "AA" },
          { key: "7", label: "AA+", value: "AA+" },
          { key: "8", label: "AAA", value: "AAA" },
          { key: "9", label: "AAA+", value: "AAA+" },
          { key: "10", label: "S", value: "S" }
       ]
    },
    scoregap(){
      return [
        { key: "0", label: "scoregap", value:"scoregap" }
      ]
    }
  },

  methods: {
    SendDatas: function () {
      var data = { your_id: this.your_id,
       opp_id: this.opp_id,
       minlevel: this.selected_minlevel,
       maxlevel: this.selected_maxlevel,
       difficulty: this.selected_diff,
       clearmark: this.selected_clearlamp,
       grade: this.selected_grade,
       scoregap: this.selected_scoregap}

      axios
        .post('/post', data)
        .then(response => {
          this.items.push(response.data)
        })
    }
    // SendData: function () {
    //   var data = { user1: this.InputUser1,
    //    user2: this.InputUser2,
    //    difficulty: this.InputDifficulty,
    //    gap: this.InputScoreGap}

    //   axios
    //     .post('/post', data)
    //     .then(response => {
    //       this.items.push(response.data)
    //     })
    //     .catch(err => {
    //       alert('APIサーバと接続できません')
    //       err = null
    //     })
    // }
  }
}
</script>