package main

import "fmt"

type taskList struct {
	tasks []*task
}

func (t *taskList) listAdd(tl *task) {
	t.tasks = append(t.tasks, tl)
}
func (t *taskList) listDelete(index int) {
	t.tasks = append(t.tasks[:index], t.tasks[index+1:]...)
}

func (t *taskList) printList() {
	for _, task := range t.tasks {
		fmt.Println("name:", task.name, " Description:", task.description)
	}
}

func (t *taskList) printListComplete() {

	for _, task := range t.tasks {
		if task.completado {
			fmt.Println("name:", task.name, " Description:", task.description)
		}
	}
}

type task struct {
	name        string
	description string
	completado  bool
}

func (t *task) completeTask() {
	t.completado = true
}

func (t *task) descriptionUpdate(description string) {
	t.description = description
}

func (t *task) nameUpdate(name string) {
	t.name = name
}

func main() {

	t0 := &task{
		name:        "completar mi curso de Go",
		description: "Curso de Platzi",
	}
	t1 := &task{
		name:        "completar mi curso de python",
		description: "Curso de Platzi",
	}

	list := &taskList{
		tasks: []*task{
			t0, t1,
		},
	}

	t2 := &task{
		name:        "completar mi curso de nodejs",
		description: "Curso de Platzi",
	}

	list.listAdd(t2)
	list.tasks[1].completeTask()
	list.printListComplete()

	mapTask := make(map[string]*taskList)

	mapTask["Robin"] = list

	t3 := &task{
		name:        "completar mi curso de Java",
		description: "Curso de Platzi",
	}
	t4 := &task{
		name:        "completar mi curso de C#",
		description: "Curso de Platzi",
	}

	listB := &taskList{
		tasks: []*task{
			t3, t4,
		},
	}
	mapTask["Ricardo"] = listB

	fmt.Println("tareas de Robin")
	mapTask["Robin"].printList()
	fmt.Println("tareas de Ricardo")
	mapTask["Ricardo"].printList()
}
