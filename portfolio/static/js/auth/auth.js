angPortfolio.factory('AuthService', function ($http, $q, $window) {
    var authenticate = function (username, password, endpoint) {
        var url = '/users/' + endpoint;
        var deferred = $q.defer();
        $http.post(url, 'username=' + username + '&password=' + password, {
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded'
            }
        })
        .then(
            function (response) {
                console.log(response);
                var token = response.data.user_token;
                var username = response.data.username;
                var user_id = response.data.id;

                if (token && username) {
                    $window.localStorage.token = token;
                    $window.localStorage.username = username;
                    $window.localStorage.user_id = user_id;
                    deferred.resolve(true);
                } else {
                    deferred.reject('Invalid data received from server');
                }
            }
        //        ,function (response) {
        //            deferred.reject(response.data.error);
        //            console.log(response);
        //        }
        );
            return deferred.promise;
    };

    var logout = function () {
        var deferred = $q.defer();
        var url = '/users/logout/';

        $http.post(url).then( function () {
            $window.localStorage.removeItem('token');
            $window.localStorage.removeItem('username');
            deferred.resolve();
        }, function (error) {
            deferred.reject(error.data.error);
        });
        return deferred.promise;
    };

    return {
        register: function (username, password) {
            return authenticate(username, password, 'register/');
        },
        login: function(username, password){
            return authenticate(username, password, 'login/');
        },
        logout: function(){
            return logout();
        }
    };
});