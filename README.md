# svelte-flask

Template for flask backend with svelte frontend components.

## Setup

### Setup flask backend
* Create new python environment: `python3 -m venv venv`
* Activate environment: `source venv/bin/activate`
* Upgrade pip: `python -m pip install --upgrade pip`
* Install flask: `pip install flask`

### Setup svelte frontend client
* In the root project folder, use `npx degit sveltejs/template client` to create a new directory called `client` and copy svelte inside it
* Inside `client`, run `npm install` to install svelte
* Use `npm run dev` to confirm that the installation worked
* Use `npm run build` to build svelte each time svelte files are modified and saved


## Running the app locally

Running the backend:
* `export FLASK_APP=app`
* `export FLASK_ENV=development`
* `flask run`

After svelte code is compiled into the `build` directory and flask routes are pointed at these files, running the flask backend will allow serving of svelte files.

