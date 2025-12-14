本节课介绍了 Python 中原生的协程，主要讲解了 `async` 和 `await` 关键词的使用。在 Python 3.5 之前，协程主要是通过生成器（generator）和 `yield` 语句实现的，这种方式虽然可以完成任务，但代码逻辑较为混乱，不利于维护。为了使代码的语义更加明确，Python 3.5 引入了 `async` 和 `await` 关键词，用于定义和调用原生协程。

- `async` 关键词用于定义一个协程函数，如 `async def download_url(url)`。
- `await` 关键词用于在一个协程函数中等待另一个协程的执行结果，如 `html = await downloader(url)`。

通过 `async` 和 `await`，Python 将协程与生成器严格区分开来，避免了代码的混乱，使协程的实现更加清晰。此外，原生协程不能直接使用 `yield` 语句，只能使用 `await` 来等待 `awaitable` 对象。

最后，为了兼容旧的生成器协程，可以使用 `@types.coroutine` 装饰器将生成器转换为可被 `await` 调用的对象。

本节内容为理解协程的语义和使用提供了基础，下一节将对本章内容进行总结。