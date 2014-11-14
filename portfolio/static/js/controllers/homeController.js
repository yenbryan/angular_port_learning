function homeController($scope, ProjectFactory, $window, $location) { //portfolioProject) { //$routeParams
//        portfolioProject.get()
//            .$promise
//            .then(function(response){
//                $scope.portfolioProjects = response.results;
//                $scope.projectResponse = response;
//
//            });
      $scope.current_user_id = $window.localStorage.user_id;
      $scope.current_user = $window.localStorage.username;
      $scope.currentPage = 1;
      $scope.itemPerPage = 5;

      $scope.setPage = function (pageNo) {
        $scope.currentPage = pageNo;
      };

      $scope.pageChanged = function() {
          ProjectFactory.getProjects($scope.currentPage)
                .then(function (response) {
                    $scope.totalItems = response.data.count;
                    $scope.portfolioProjects = response.data.results;
                });
      };

      $scope.pageChanged();
      $scope.maxSize = 5;
      $scope.bigTotalItems = 175;
      $scope.bigCurrentPage = 1;

      $scope.follow = function(project_id) {
            ProjectFactory.follow(project_id)
                .then( function(res){
                    console.log(res);
                    $location.path('/');
                });
      };

      $scope.unfollow = function(project_id) {
            ProjectFactory.unfollow(project_id)
                .then( function(res){
                    $location.path('/');
                });
      };
}