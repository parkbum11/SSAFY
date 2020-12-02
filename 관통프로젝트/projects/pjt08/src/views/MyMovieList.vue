<template>
  <div>
    <h1>My Movie List</h1>
    <b-container>
      <MyListForm @onMovieDataChange="onMovieListChange"/>
          <MyList 
      v-for="(movieList, idx) in movieLists" 
      :key="idx"
      :movieList="movieList"
      @deleteMovieList="changeSeenMovieStatus"
      @ondeleteMovie="deleteMovie"
      />
    </b-container>
    

  </div>
</template>
onMovieListChange
<script>
import MyListForm from '../components/MyListForm.vue'
import MyList from '../components/MyList.vue'
// import func from '../../vue-temp/vue-editor-bridge'

export default {
  name: 'MyMovieList',
  components: {
    MyListForm,
    MyList,
  },
  data() {
    return {
      movieLists: []
    }
  },
  methods: {
    onMovieListChange: function(MovieListData) {
    for (let index = 0; index < this.movieLists.length; index++) {
      if(MovieListData==this.movieLists[index].title){
        alert("This movie is already on the list!")
        return
      }
      else if (MovieListData === '') {
        alert("Please enter a movie!")
        return
      }
    }
    this.movieLists.push({title: MovieListData, seenMovie: false})
    },
    changeSeenMovieStatus: function(movieList) {
      const index = this.movieLists.indexOf(movieList)
      this.movieLists[index].seenMovie=!this.movieLists[index].seenMovie
    },
    deleteMovie: function(mList) {
      const index = this.movieLists.indexOf(mList)
      this.movieLists.splice(index, 1)
    }
  }
}
</script>

<style>

</style>