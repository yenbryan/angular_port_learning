angPortfolio.factory('ProjectFactory', function($http) {
    return {
//        repoList: [],
        getProjects: function(page){
            return $http.get('http://127.0.0.1:8000/projects/?page='+page);
        },
        follow: function(id){
            return $http.post('http://127.0.0.1:8000/projects/'+id+'/follow/');
        },
        unfollow: function(id){
            return $http.delete('http://127.0.0.1:8000/projects/'+id+'/unfollow/');
        }
    }
});