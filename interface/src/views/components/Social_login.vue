<template>
  <div>
    <g-signin-button
        v-if="isEmpty(user)"
        :params="googleSignInParams"
        @error="onGoogleSignInError"
        @success="onGoogleSignInSuccess"
    >
      <button class="btn btn-block btn-success">
        Google Signin
      </button>
    </g-signin-button>
    <div style="margin: 0 auto; width: 700px; align-content: center">
      <v-facebook-login app-id="187272676634276" @sdk-init="handleSdkInit"></v-facebook-login>
      <facebooklogin></facebooklogin>
    </div>
  </div>
</template>

<script>
// TODO：需要重新写前端FB注册
import VFacebookLogin from 'vue-facebook-login-component';
import axios from 'axios'
import Facebooklogin from "@/views/components/facebook-login";

export default {
  name: "Login",
  data() {
    return {
      user: {},
      googleSignInParams: {
        client_id: '690024386674-cpkugdn9h578rkollmjujuhj54db0v54.apps.googleusercontent.com'
      },
      FB: {},
      model: {},
      scope: {},
    }
  },
  components: {
    Facebooklogin,
    VFacebookLogin
  },
  methods: {
    onGoogleSignInSuccess(resp) {
      console.log(resp)
      const token = resp.qc.access_token
      axios.post('http://localhost:8000/api-auth/convert-token', {
        token: token,
        backend: "google-oauth2",
        grant_type: "convert_token",
        client_id: "rAR0ef1StYXJDaEjDQMT7i5MuF7PhSZ1qY5cFD0S",
        client_secret: "YcEykooagJTwYYj4I0yhk5xnNwBJOtCKkBsjdFUTkp40eVWrjTNrydhVbhBnCs93niVxoXXCZXnlhLrNRdsyv3ayzJJOgSxeBOh13iFHa91I45U47RQFxsKNxpibutiB",
      })
          .then(resp => {
            console.log(resp)
            this.user = resp.data
            this.$route.push()
          })
          .catch(err => {
            console.log(err.response)
          })
    },
    onGoogleSignInError(error) {
      console.log('OH NOES', error)
    },
    isEmpty(obj) {
      return Object.keys(obj).length === 0
    },
    handleSdkInit({FB, scope}) {
      this.FB = FB
      console.log(FB)
      this.scope = scope
      // axios.post('http://localhost:8000/api-auth/convert-token', {
      //   token: token,
      //   backend: "google-oauth2",
      //   grant_type: "convert_token",
      //   client_id: "rAR0ef1StYXJDaEjDQMT7i5MuF7PhSZ1qY5cFD0S",
      //   client_secret: "YcEykooagJTwYYj4I0yhk5xnNwBJOtCKkBsjdFUTkp40eVWrjTNrydhVbhBnCs93niVxoXXCZXnlhLrNRdsyv3ayzJJOgSxeBOh13iFHa91I45U47RQFxsKNxpibutiB",
      // })
    }
  }
}
</script>

<style scoped>

</style>
