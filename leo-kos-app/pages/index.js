import Head from 'next/head'
import Image from 'next/image'
import styles from '../styles/Home.module.css'

export default function Home() {
  return (
    <div className={styles.container}>
      <Head>
        <title>Leo & Kos</title>
        <meta name="description" content="A site for us and our boys" />
        <link rel="icon" href="/favicon.ico" />
      </Head>

      <main className={styles.main}>
        <h1 className={styles.title}>
          Leo & Kos
        </h1>
      </main>

      <footer className={styles.footer}>

      </footer>
    </div>
  )
}
