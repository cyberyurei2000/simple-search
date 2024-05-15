from threading import Thread
from glob import glob
import os, time

results = []
limit = 0


def run(path: str, user: str, type: str, max_limit: str | int) -> None:
    global limit
    os.chdir(path)
    if limit < int(max_limit):
        if len(is_subdir(path)) != 0:
            task(path, user, type, int(max_limit), False)
            for folder in next(os.walk(path))[1]:
                th = Thread(target=task,
                            args=(
                                f"{path}{folder}/",
                                user,
                                type,
                                int(max_limit),
                            ))
                th.start()
                th.join()
        else:
            task(path, user, type, int(max_limit))


def task(path: str,
         user: str,
         type: str,
         max_limit: str | int,
         multiple=True) -> None:
    global limit
    os.chdir(path)

    match type:
        case "name":
            for name in glob(f"*{user}*.*"):
                if limit < int(max_limit):
                    results.append(f"{path}{name}")
                    limit += 1
                else:
                    break
        case "ext":
            for ext in glob(f"*.{user}"):
                if limit < int(max_limit):
                    results.append(f"{path}{ext}")
                    limit += 1
                else:
                    break
        case "date":
            for file in list(glob("*.*")):
                if limit < int(max_limit):
                    ctime = time.ctime(os.path.getctime(file))
                    file_t = time.strftime("%d/%m/%Y", time.strptime(ctime))
                    if file_t == user:
                        results.append(f"{path}{file}")
                        limit += 1
                else:
                    break
        case "size":
            for file in list(glob("*.*")):
                if limit < int(max_limit):
                    file_s = os.path.getsize(f"{path}{file}")
                    if str(file_s) == user:
                        results.append(f"{path}{file}")
                        limit += 1
                else:
                    break
        case "str":
            for file in list(glob("*.*")):
                if limit < int(max_limit):
                    with open(file, "r") as file_:
                        if user in file_.read():
                            results.append(f"{path}{file}")
                            limit += 1
                else:
                    break

    if multiple:
        if limit < int(max_limit):
            if len(is_subdir(path)) != 0:
                run(path, user, type, int(max_limit))


def is_subdir(path) -> list[str]:
    os.chdir(path)
    return next(os.walk('.'))[1]


def get_results() -> list[str]:
    #string = "".join([f"{str(item)}\n" for item in results])
    string = [str(item) for item in results]
    reset()
    return string


def reset() -> None:
    global limit
    limit = 0
    results.clear()
