var authController = function ($scope, $location, AuthService) {
  $scope.register = function () {
    var username = $scope.registerUsername;
    var password = $scope.registerPassword;

    if (username && password) {
      AuthService.register(username, password)
          .then(function () {
                    $location.path('/');
                },
                function (error) {
                    $scope.registerError = error;
          });
    } else {
      $scope.registerError = 'Username and password required';
    }
  };

  $scope.login = function(){
    var username = $scope.loginUsername;
    var password = $scope.loginPassword;

    if(username && password){
        AuthService.login(username, password)
            .then(function(){
                $location.path('/');
            },function(){
                console.log('failed');
            });
    }
  };

};