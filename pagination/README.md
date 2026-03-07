# Pagination

This directory contains exercises and examples about **pagination**—a common pattern for returning large collections of data in smaller, manageable chunks.

Pagination improves performance and user experience by:
- Reducing payload size
- Avoiding long response times
- Making APIs easier to consume in UI/clients

## Learning Objectives

By completing the tasks in this folder, you should be able to:
- Explain why pagination is needed for APIs and data-heavy applications
- Implement different pagination strategies
- Validate and normalize pagination parameters
- Return consistent, predictable paginated responses

## Concepts Covered

### 1) Page / Limit (Offset-based)

A simple and widely used approach:
- `page`: which page to return (typically starting at 1)
- `page_size` / `limit`: how many items per page

This is easy to implement but can become less efficient on very large datasets because it relies on offsets.

### 2) Offset / Limit

Similar to page/limit, but directly uses an offset:
- `offset`: number of items to skip
- `limit`: number of items to return

### 3) Cursor-based Pagination

Uses a stable cursor (e.g., a record ID or timestamp) to fetch the next set of results. This is generally more reliable for frequently changing datasets.

## Expected API Behavior (Recommended)

When building a paginated endpoint, it is recommended to return metadata along with results, for example:
- `page`
- `page_size`
- `total_items`
- `total_pages`
- `next_page` / `prev_page` (or `next_cursor`)
- `data` (the list of items)

## How to Run

This project is part of the **Holberton School Web Back End** curriculum. Follow the repository-level instructions to run the specific scripts in this directory.

## Files

- This folder contains multiple tasks/scripts related to pagination.
- Refer to each task file for usage details and expected outputs.

## Author

- Abdulrhman Alghamdi
