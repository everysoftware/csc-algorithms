# Деревья

## Задачи

| Задача          | Код           |
|-----------------|---------------|
| Обход в глубину | `dfs`         |
| Высота дерева   | `tree_height` |

## Деревья

**Дерево** - это иерархическая структура данных, состоящая из вершин (узлов) и ребер, которые их соединяют.
Деревья подобны графам, однако, ключевое отличие дерева от графа таково: в дереве не бывает циклов.

Деревья широко используются в области искусственного интеллекта и в сложных алгоритмах, выступая в качестве эффективного
хранилища информации при решении задач.
Двоичное дерево - это дерево, в котором каждая вершина имеет не более двух потомков.

## Обход в глубину

**DFS** (Depth-First Search) - обход в глубину - это алгоритм обхода графа или дерева, который начинается с начальной
вершины и идет вглубь каждой ветви, пока не достигнет конечной вершины.
Сложность DFS: O(N), N = V + E, где V - количество вершин, E - количество ребер.

Пример

```text
A : B, C
B : D, E
C : F
```

Визуализируем дерево:

```text
    A
   / \
  B   C
 / \   \
D   E   F
```

Обход в глубину начинается с вершины A и проходит по всем вершинам графа:

```text
A -> B -> D -> E -> C -> F
```
