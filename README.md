# Data Structures and Algorithms

- [Chap01](./chap01): Recursive function
- [Chap03](./chap02): OOP
- [Chap03](./chap03): Array list
- [Chap04](./chap04): Stack
- [Chap05](./chap05): Circular structure
- [Chap06](./chap06): Linked structure
- [Chap07](./chap07): Sorting Algorithms
- [Chap08](./chap08): Binary search tree

---

## [Nodemon](https://nodemon.io/)

A utility that monitors changes in your source code and automatically restarts
your application. Mainly for **Node.js**.

### Prerequisite

Download and Install **[Node.js](https://nodejs.org/)**.

### Install

Install globally to use it everywhere without creating `node_modules/`.

```sh
npm install -g nodemon

nodemon --version
```

### Configure

For advanced configurations, create a `nodemon.json` file inside your project.

> **NOTE**
>
> Nodemon will not work properly if it uses `JSONC` extension.

Watch **python** files under **chap08** directory and when change is detected,
**exec** the command. And **clear** the terminal on every run.

```json
{
  "watch": ["chap08"],
  "ext": "py",
  "ignore": [],
  "exec": "python3 ./chap08/binary_tree.py",
  "events": {
    "start": "clear"
  }
}
```

- `watch`: Files or directories to monitor.
- `ext`: File extensions to watch.
- `ignore`: Path to exclude.
- `exec`: Command to run on changes.
- `start`: Command to run on start.

### Run

From where the **nodemon.json** is at:

```sh
nodemon
```

Enter `rs` to restart without changing the codes.
