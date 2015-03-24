var phonecatApp = angular.module('phonecatApp', [])


phonecatApp.controller('TaskCtrl', ['$scope', '$http', '$timeout',
  function($scope, $http, $timeout) {
    $scope.refresh_func = function() {
      $http.get('/apiv1/tags').success(function(data) {
        $timeout(function() {
          $scope.tags = data;
        });
      });
    };

    $scope.tasks = [
      {taskText:'learn angular', done:true},
      {taskText:'build an angular app', done:false}];
    $scope.phones = "Hello";

    $scope.addTag = function(newTag) {
      tagModel = {}
      tagModel.tag_name = newTag;
      $http.post('/apiv1/tags', angular.toJson(tagModel)).success(function(data) {
        $scope.tag_success = 'success';
      });
    };

    $scope.removeTag = function(tagKey) {
      $http.delete('/apiv1/tags')
    }
    $scope.tag_success = "none";

    (function() {
      $scope.refresh_func();
    })();

}]);


function TaskCtrl2($scope) {


  $scope.addTask = function() {
    $scope.tasks.push({taskText:$scope.taskInputText, done:false});
    $scope.taskInputText = '';
  };

  $scope.remaining = function() {
    var count = 0;
    var a = 3 + 2

    angular.forEach($scope.todos, function(todo) {
      count += todo.done ? 0 : 1;
    });
    return count;
  };

  $scope.archive = function() {
    var oldTodos = $scope.todos;
    $scope.todos = [];
    angular.forEach(oldTodos, function(todo) {
      if (!todo.done) $scope.todos.push(todo);
    });
  };
}

