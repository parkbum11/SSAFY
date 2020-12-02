<template>
  <div id="styling" class="loginbg">
    <form @submit="login">
      <h1>Log In</h1><br>

      <div class="form-group">
        <label>Name</label>
        <input v-model="username" type="text" class="form-control form-control-lg" />
      </div>

      <div class="form-group">
        <label>Password</label>
        <input v-model="password" type="password" class="form-control form-control-lg" />
      </div>
      <br>
      <button type="submit" class="btn btn-primary btn-lg btn-block">Log In</button>
      
      <p class="forgot-password text-right mt-2 mb-4 text-white">
        <router-link to="/signup">아직 회원가입을 안하셨나요 ?</router-link>
      </p>
      <hr style="border:solid 1px white">
      <p>다른 방법으로 로그인 하기</p>
      <div class="social-icons">
        <ul>
          <li><a href="#"><i class="fa fa-google"></i></a></li>
          <li><a href="#"><i class="fa fa-facebook"></i></a></li>
          <li><a href="#"><i class="fa fa-twitter"></i></a></li>
          <!-- <li><a href="#"><i class="fa fa-kakao"></i></a></li> -->
        </ul>
      </div>

    </form>
  </div>
</template>

<script>
import axios from 'axios'
import Swal from 'sweetalert2'

export default {
  data() {
    return { username: '', password: '',}
  },
  methods: {
    login(event) {
      event.preventDefault()
      axios({
        url: 'http://127.0.0.1:8000/accounts/api-token-auth/',
        method: 'POST',
        data: { username: this.username, password: this.password, },
      }).then((res) => {
        localStorage.setItem('jwt', res.data.token)
        this.$store.commit('USER_NAME', this.username )
        this.$router.push('/')
        Swal.fire({
          title: `환영합니다 ${this.username} 님! \n The Movie의 새로운 영화를 \n 추천 받아 보세요!`,
          text: '',
          icon: 'success',
          confirmButtonText: '확인'
        })
      }).catch(()=>{
        console.log(this.username, this.password)
        if (this.username == '') {
          Swal.fire({
            title: 'Error',
            text: '아이디를 입력해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        } else if (this.password == '') {
          Swal.fire({
            title: 'Error',
            text: '비밀번호를 입력해주세요',
            icon: 'error',
            confirmButtonText: '취소'
          })
        }
      })
    }
  }
}
</script>

<style>
#styling {
  display: flex;
  height: 100vh;
  justify-content: center;
  align-items: center;
}

.loginbg {
  background-image: 
    linear-gradient( rgba(0, 0, 0, 0.55), rgba(0, 0, 0, 0.55) ), url('../assets/loginbg.png');
  background-size: cover;
  opacity: 1;
}

form {
  color: white;
}

.social-icons {
  text-align: center;
  font-family: "Open Sans";
  font-weight: 300;
  font-size: 1.5em;
  color: #222222;
}

.social-icons ul {
  list-style: none;
  margin: 0;
  padding: 0;
}
.social-icons ul li {
  display: inline-block;
  zoom: 1;
  width: 65px;
  vertical-align: middle;
  border: 1px solid #e3e8f9;
  font-size: 15px;
  height: 40px;
  line-height: 40px;
  margin-right: 5px;
  background: #11ffee00;
}

.social-icons ul li a {
  display: block;
  font-size: 1.4em;
  margin: 0 5px;
  text-decoration: none;
}
.social-icons ul li a i {
  -webkit-transition: all 0.2s ease-in;
  -moz-transition: all 0.2s ease-in;
  -o-transition: all 0.2s ease-in;
  -ms-transition: all 0.2s ease-in;
  transition: all 0.2s ease-in;
}

.social-icons ul li a:focus i,
.social-icons ul li a:active i {
  transition: none;
  color: #11ffee00;
} 
</style>