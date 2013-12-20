# steak.py

**Simplify writing and executing repetitive tasks.**

Steak is a minimal and powerful utility for collecting all of your mindless,
repetitive tasks into a single, brilliantly-named `steakfile`. As an evolution
of [bumpy](https://github.com/scizzorz/bumpy), steak focuses on the same design
principles - minimize friction when writing tasks and provide a simple CLI
interface to execute your tasks.

Inspired by tools like [nose](https://github.com/nose-devs/nose/), steak allows
you to write plain Python functions which will be automatically discovered and
prepared for execution. By inspecting your function signatures, steak learns as
much as it can and provides a simple and understandable command line interface
to your tasks without requiring any extra effort on your end.

## Usage

### Write a `steakfile` / `grill.py`

Toss the code below in a `steakfile` or `grill.py`.

```python
def build():
	'''Builds ALL THE CODE.'''
	print('Building...')

def run():
	'''Runs ALL THE PROGRAMS.'''
	build()
	print('Running...')

def clean():
	'''Cleans ALL THE GARBAGE.'''
	print('Cleaning...')
```

### Execute your tasks

Just call the included `grill` command-line tool to run your tasks.

```bash
$ grill build
Building...
$ grill run
Building...
Running...
$ grill clean
Cleaning...
```

### Execute several tasks

Give multiple space-separated task names to `grill` to execute them all.

```bash
$ grill build run
Building...
Running...
```

Notice that `grill` tries to avoid repeating task execution, so it only runs
the `build` task once! You can explicitly run a task multiple times.

```bash
$ grill build build run
Building...
Building...
Running...
```

### Save some keystrokes

Steak will allow you to abbreviate command names as much as you want, but if
there's ambiguous tasks, the task selection behavior is unreliable.

```bash
$ grill b r
Building...
Running...
```
### Get some help

If you invoke `grill` with no arguments, an automatic help message will be
printed out.

```bash
$ grill
build
	Builds ALL THE CODE.
clean
	Cleans ALL THE GARBAGE.
run
	Runs ALL THE PROGRAMS.
```
