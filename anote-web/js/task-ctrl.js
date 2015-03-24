var phonecatApp = angular.module('phonecatApp', [])

var TAG_API_URL = '/apiv1/tag';
var PROJECT_API_URL = '/apiv1/project';

phonecatApp.controller('TaskCtrl', ['$scope', '$http', '$timeout',
  function($scope, $http, $timeout) {
    $scope.refresh_func = function() {
      $http.get(TAG_API_URL).success(function(data) {
        $timeout(function() {
          $scope.tags = data;
        });
      });

      $http.get(PROJECT_API_URL).success(function(data) {
        $timeout(function() {
          $scope.projects = data;
        });
      });
    };

    $scope.addTag = function(newTag) {
      tagModel = {}
      tagModel.tag_name = newTag;
      $http.post(TAG_API_URL, angular.toJson(tagModel)).success(function(data) {
        $scope.tag_success = 'success';
        $scope.tags.push(data);
      });
      $scope.newTag = "";
    };

    $scope.removeTag = function(tagKey) {
      $http.delete(TAG_API_URL, {params: {'key': tagKey}}).success(function(data) {
        $timeout(function() {
          for (i=0; i<$scope.tags.length; i++) {
            if ($scope.tags[i].key === tagKey) {
              $scope.tags.splice(i, 1);
              break;
            }
          }
        });
      });
    };

    $scope.addProject = function(newProject) {
      projectModel = {}
      projectModel.project_name =  newProject;
      $http.post(PROJECT_API_URL, angular.toJson(projectModel)).success(function(data) {
        $scope.projects.push(data);
      });

      $scope.newProject = "";
    };

    $scope.removeProject = function(projectKey) {
      $http.delete(PROJECT_API_URL, {params: {'key': projectKey}}).success(function(data) {
        $timeout(function() {
          for (i=0; i<$scope.projects.length; i++) {
            if ($scope.projects[i].key === projectKey) {
              $scope.projects.splice(i, 1);
              break;
            }
          }
        });
      });
    };

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

