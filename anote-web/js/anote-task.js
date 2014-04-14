function TodoCtrl($scope) {
  $scope.tasks = [
    {taskText:'learn angular', done:true},
    {taskText:'build an angular app', done:false}];

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

