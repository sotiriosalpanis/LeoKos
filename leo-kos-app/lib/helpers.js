

const slugify = (term) => {
  const slug = term.split(' ').join('')

  return encodeURIComponent(slug)
};

export {
  slugify,
};